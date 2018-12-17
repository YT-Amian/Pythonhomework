from flask import Flask, render_template, request, escape
from finding import find

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    title = 'your results:'
    results = find(phrase)
    titles = ('name', 'id')
    return render_template('view.html',
                           the_title='搜索结果',
                           the_row_titles=titles,
                           the_data=results,)


@app.route('/')
@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('records.log') as log:
        for line in log:
            contents.append([])
            for item in line.split(','):
                contents[-1].append(escape(item))
    titles = ('username',)
    return render_template('viewlog.html',
                           the_title='搜索',
                           the_title2='班级表单',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
