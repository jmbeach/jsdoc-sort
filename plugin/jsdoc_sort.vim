let g:jsdoc_sort_path = expand('<sfile>:p:h') . '/jsdoc_sort.py'
if !has('python') && !has('python3')
	echo "Error: JsdocSort requires vim compiled with +python or +python3"
	finish
endif

function! JsdocSort()
	execute (has('python3') ? 'py3file' : 'pyfile') g:jsdoc_sort_path
endfunction
