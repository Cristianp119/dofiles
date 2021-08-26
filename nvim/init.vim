" >>> mi configuracion de neovim <<< "
set number
set title 
set mouse=a 
set nowrap 
set colorcolumn=120
set hidden
syntax enable 
set showcmd 
set encoding=utf-8
set showmatch 
set sw=2


call plug#begin('~/.vim/plugged')

"IDE"
Plug 'easymotion/vim-easymotion' 
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'
Plug 'vim-airline/vim-airline' 
Plug 'vim-airline/vim-airline-themes'
call plug#end()

let NERDTreeQuitOnOpen=1
let g:airline#extensions#tabline#enabled = 1
let g:airline_theme='night_owl'
let g:airline_powerline_fonts = 1
let mapleader=" "

" >>> Mapas de atajos <<< "
nmap <Leader>s <Plug>(easeymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>
nmap <Leader>w :w<CR> 
nmap <Leader>q :q<CR>
nmap <Leader>x :x<CR>
