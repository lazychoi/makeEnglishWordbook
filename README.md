# make english wordbook 
---------------

'make english wordbook 서블라임 텍스트(Sublime Text) 3 플러그인'은 단어장을 입력하는 고통을 덜어주기 위해 만들었습니다. 'make english wordbook'을 이용해 만든 단어장 파일을 Flashcards Deluxe나 Quizlet과 같은 플래시카드 어플로 외우면 효율적으로 단어를 암기할 수 있을 것입니다.

## 영어 사전 파일

이 플러그인을 이용하려면 사전 파일(eng_dic_data.txt)을 열어두어야 합니다.

사전파일은 '영단어와 한글 풀이'로 이루어져 있고 영단어와 한글 풀이 사이는 tab문자로 구분되어 있습니다. 예를 들면 다음과 같습니다. 보기에는 스페이스바로 한 칸 띄운 것과 그다지 구분되지 않지만 마우스로 드래그하여 선택 영역을 지정하면 tab문자는 선이 표시됩니다. 

	A	a 하나의, 어느 하나의, 어떤(a certain), 같은
	a big deal	대단한 것, 중대 사건, 큰 거래
	A chromosome	x A염색체(과잉 염색체 이외의 보통 염색체)
	A level	상급학년시험
	A line	라인의, A라인의(여성복이 A자처럼 위가 좁고 밑이 퍼짐)
	a tasty morsel	맛좋은 소량의 음식

**사전 파일의 이름을 바꾸거나 형식을 수정하면 플러그인이 제대로 작동하지 않습니다.** 아래 링크한 사전 파일은 인터넷에 떠도는 파일을 약간 수정한 것입니다. 위 형식만 유지한다면 자신에게 맞는 사전 파일을 만들 수 있을 것입니다.

[사전 파일 받기](http://lazychoi.github.io/data/eng_dic_data.txt)

## 단어장 만들기

단어장도 위와 같이 탭(tab)으로 구분되는 형식으로 만듭니다. 이런 형식으로 만들면 엑셀이나 Quizlet 같은 프로그램에 복사할 때 자동으로 열(column)로 구분되어 붙습니다. 

## 기능

이 플러그인은 7가지 기능을 제공합니다. 단축키는 맥 사용자 기준입니다. 윈도우 사용자는 super 대신 alt키를 누르면 됩니다. 기본 사용법은 사전 파일을 열어 놓고 새로 단어장 파일을 만듭니다. 단어장에 단어를 입력하고 난 후 단축키를 누릅니다. 한 단어일 때는 단축키만 누르면 되지만, 여러 단어일 때는 블록을 지정한 다음에 눌러야 합니다. 그러면 새로운 창이 뜨고 그 안에서 적절한 풀이를 선택하면 단어장에 입력이 됩니다.

1. [shift + super + j] : 현재 커서가 위치한 단어나 블록으로 지정한 단어들의 풀이를 사전 파일에서 찾아 표시합니다. 이 중에서 하나를 선택하면 단어장에 입력됩니다.
2. [shift + super + m] : 사전 파일에 오타나 부적절한 설명이 있을 수 있습니다. 단어장에서 수정한 후 사전 파일에서 해당 단어를 찾아 블록으로 지정합니다. 붙여넣기만 누르면 수정한 내용으로 바뀝니다.
3. [shift + super + k] : 사전 파일에 단어 풀이가 없을 경우 이 키를 누르면 네이버사전이 뜹니다. 복사한 후 단어장에 입력합니다. (인터넷이 연결되어 있어야 합니다.)
4. [shift + super + i] : 사전 파일에 단어 풀이를 추가합니다. 

아래 세 기능은 단어가 포함된 문장을 복사하는 기능입니다. 따라서 텍스트 파일로 된 원서가 있을 경우 사용합니다. 한 줄 전체를 불러오니 문장별로 나눠두어야 합니다.

5. [shift + super + o] : 단어가 포함된 문장을 커서가 있는 줄의 맨 끝에 입력합니다.
6. [shift + super + h] : 단어가 포함된 문장을 불러오는데 단어를 빨간색으로 진하게 강조합니다. 단어를 암기할 때 문맥을 활용할 수 있을 것입니다.
7. [shift + super + u] : 단어가 포함된 문장을 불러오는데 단어를 밑줄로 바꿉니다. 단어 시험을 볼 때 유용하게 사용할 수 있을 것입니다.


This plugin for sublime text 3 is to help making english-korean wordbook.
To use this plugin, you have to open the english-korean dictionary file--eng_dic_data.txt.
And then you can create new wordbook file which name is in your hand.

This plugin has seven functions.

1. [shift + super + j] : After you enter a word to lookup, the quick panel displays the definition of the word in the eng_dic_data file. You can select definition suit to the word, and the definition is inserted to your wordbook.

2. [shift + super + i] : When there is no word you will find, you can insert word and definition into the dictionary file.

3. [shift + super + m] : You can move to the source definition when you change dictionary file.

4. [shift + super + k] : You can lookup the word in Naver dictionary.

5. [shift + super + o] : You can copy sentence which contains keyword to the end of the line in wordbook.

6. [shift + super + h] : You can copy sentence which contains keyword to the keyword position in wordbook with highlighting html tag.

7. [shift + super + u] : You can copy sentence which contains keyword to the keyword position in wordbook with converting keyword into blank.

Windows users have to use alt key for super.