# Latex_Vorlage
## Latex Cheat Sheet
Siehe: https://wch.github.io/latexsheet/

# Ordnerstruktur
* **ads/** - enthält die notwendigen Seiten, z.B. Abstract, Deckblatt etc., sowie einige Interna
	* **ads/glossary.tex** - Glossareinträge
	* **ads/acronyms.tex** - Einträge des Abkürzungsverzeichnisses
* **content/** - enthält pro Kapitel eine Datei (Schema: `<nn>kapitel.tex`)
* **images/** - enthält Bilder und Logos
	* **images/logo.png** - Logo der Firma auf Deckblatt.
* **einstellungen.tex** - hier werden z.B. die Pflichtangaben auf dem Deckblatt geändert
* **dokumentation.tex** - die Hauptdatei, die alles andere einbindet
* **bibliographie.bib** - Einträge der Bibliographie
* **latexmkrc** - die Regeln, nach denen latexmk das Dokument baut

# Vorlage verwenden
Pflichtangaben und einige weitere Einstellungen können in `einstellungen.tex` geändert werden. Kapitel werden in `content` nach dem Schema `<nn>kapitel.tex` angelegt, wobei &lt;nn&gt; eine mindestens zweistellige Zahl sein muss.

## Kommentare
Kommentare können mit dem Befehl `\comment{Kommentar}` verfasst werden. Diese heben sich durch eine blaue Schriftfarbe hervor.

## TODOS / Notizen
Hervorgehobene Notizen können mit den folgenden Befehlen umgesetzt werden:
1. `\todo{Notiz}` entspricht einer gelben Markierung am rechten Rand mit entsprechendem Inhalt.
2. `\todo[inline]{Notiz}` entspricht einer gelben inline-Textbox mit entsprechendem Inhalt.

## Kennzeichnung des Autors
Es gibt zwei Möglichkeiten den Autor eines Kapitels, Abschnitts oder Paragraphen kennzuzeichnen.
1. Der Autor wird direkt nach dem Titel des Kapitels bzw. des Abschnitts in Kapitälchen genannt. Dazu können die beiden Befehle `\chapterauthor{Name}` oder `\sectionauthor{Name}` genutzt werden.
2. Der Autor wird am Ende eines Abschnitts bzw. Paragraphen rechtsbündig in Kapitälchen aufgeführt. Dazu kann der Befehl `\mentionauthor{Name}` verwendet werden.

## Verwendung von Akronymen und Glossareinträgen
### Akronyme
Akronyme werden in der Datei **ads/acronyms.tex** nach dem Schema `\acro{AKRONYM}{Ausgeschriebene Version}` angelegt und wie folgt verwendet:
* `\ac{Abk.}`   --> fügt die Abkürzung ein, beim ersten Aufruf wird zusätzlich automatisch die ausgeschriebene Version davor eingefügt bzw. in einer Fußnote (hierfür muss in header.tex \usepackage[printonlyused,footnote]{acronym} stehen) dargestellt
* `\acs{Abk.}`   -->  fügt die Abkürzung ein
* `\acf{Abk.}`   --> fügt die Abkürzung UND die Erklärung ein
* `\acl{Abk.}`   --> fügt nur die Erklärung ein
* `\acp{Abk.}`  --> gibt Plural aus (angefügtes 's'); das zusätzliche 'p' funktioniert auch bei obigen Befehlen

### Glossareinträge
Glossareinträge werden in der Datei **ads/glossary.tex** nach dem Schema `\newglossaryentry{Beispiel}{name={Beispiel},plural={Beispiele},description={Ein Beispiel für einen Glossar-Eintrag}}`´angelegt und mit den folgenden Befehlen verwendet:
* `\gls{Beispiel}` --> Fügt den Begriff im Singular mit einem Querverweis auf die Glossarseite ein
* `\glspl{Beispiel}` --> Fügt den Begriff im Plural mit einem Querverweis auf die Glossarseite ein
* `\Gls{Beispiel}` --> Fügt den Begriff im Singular mit einem Querverweis auf die Glossarseite ein (Anfangsbuchstabe groß)
* `\Glspl{Beispiel}` --> Fügt den Begriff im Plural mit einem Querverweis auf die Glossarseite ein (Anfangsbuchstabe groß)

**WICHTIG**
Damit die Glossareinträge im Dokument sichtbar sind, müssen im Stammordner (Ordner, in dem sich die dokumentation.tex Datei befindet) folgende Befehle ausgeführt werden:
* `makeglossaries dokumentation.acn`
* `makeglossaries dokumentation.glo`

# Quellcodes, Algorithmen und weitere Spezialitäten
## Quellcodes (Listings)
Quellcodes werden wie folgt eingefügt:
```
\begin{minipage}{\textwidth}
	\begin{lstlisting}[language=Rust, caption=Beispielcode, label=lst:beispielcode]
	Beipspielcode() {
		print(test)
	}
	\end{lstlisting}
\end{minipage}
```
Dabei stehen aktuell folgende Sprachen zur Auswahl:

**PHP, Python, Java, C, C++, bash, HTML, NgTS (= Angular TypeScript), CSS, ASN.1, Go, Rust, Plain**

Die Minipage-Funktion wird verwendet, damit der Quellcode nicht auf zwei Seiten verteilt wird, sondern stets als ein zusammenhängender Block eingebettet wird.

## Algorithmen
Algorithmen werden so wie im folgenden Beispiel verwendet:
```
\begin{algorithm}
\begin{algorithmic}[1]
\Procedure{Euclid}{$a,b$}\Comment{The g.c.d. of a and b}
   \State $r\gets a\bmod b$
   \While{$r\not=0$}\Comment{We have the answer if r is 0} \label{alg:euclid:while}
      \State $a\gets b$
      \State $b\gets r$
      \State $r\gets a\bmod b$
   \EndWhile\label{euclidendwhile}
   \State \textbf{return} $b$\Comment{The gcd is b}
\EndProcedure
\end{algorithmic}
\caption{Euklid'scher Algorithmus}\label{alg:euclid}
\end{algorithm}
```
## Bilder
Bilder werden mit dem folgenden Befehl eingefügt:
```
\begin{figure}[H]
	\centering
	\includegraphics[width=\imgBig]{images/theory/beispielbild.png}
	\caption{Beispielbild}
	\label{fig:beispielbild}
\end{figure} 
```
Zur festlegung der Größe (Breite) stehen folgende Marcos zur Verfügung:
* `\imgBig` = Volle Textbreite
* `\imgMed` = 15cm
* `\imgSmall` = Halbe Textbreite
* `\imgMini` = Viertel Textbreite

Mit folgendem Befehl können außerdem mehrere Bilder nebeneinander eingefügt werden:
```
\begin{figure}[H]
  \centering
  \subfloat[][]{\includegraphics[width=0.45\linewidth]{images/theory/beispiel1.png}}%
  \qquad
  \subfloat[][]{\includegraphics[width=0.45\linewidth]{images/theory/beispiel2.png}}%
  \caption{Beispielvarianten a und b}%
  \label{fig:beispiel}
\end{figure}
```
Dabei werden die eingefügten Bilder alphabetisch nummeriert.

## Labeling
Damit Querverweise innerhalb des Dokuments möglich sind, sollte jedes Objekt mit einem **Label** versehen werden. Diese sollten abhängig vom Objekttyp wie folgt benannt werden:
* Chapter: `cha:beispiel_label`
* Section: `sec:beispiel_label`
* Subsection: `ssec:beispiel_label`
* Subsubsection: `sssec:beispiel_label`
* Figure: `fig:beispiel_label`
* Listing: `lst:beispiel_label`
* Algorithm: `alg:beispiel_label`

# Zitieren
Zum Zitieren von Quellen wird Citavi 6 verwendet. Dafür habe ich bereits ein neues Projekt "Studienarbeit" angelegt. 
Um die gespeicherten Quellen verwenden zu können, muss jedem Werke ein eindeutiger **BibTex-Key** zugewiesen werden. Dieser sollte dem Schema *Nachname.Jahr* folgen, wobei bei Sammelwerken oder Gruppenpublikationen stets der erst genannte Name zu nutzen ist.
Anschließend muss die `.bib`-Datei exportiert werden und im Stammordner unter **bibliographie.bib** gespeichert werden. Zu Beginn ist bereits eine leere Datei vorhanden. Diese muss folglich überschrieben werden.

Zum Zitieren in Latex kann und wird der Befehl `\cite{BibTex-Key}` verwendet. Sollen mehrere Quellen gleichzeitig zitiert werden, so können die entsprechenden BibTex-Keys mit Kommata getrennt angegeben werden: `\cite{BibTex-Key1, BibTex-Key2,...}`. Wird eine spezielle Seite oder ein Seitenbereich zitiert, so kann dieser wie folgt spezifiziert werden: `\cite[S. 15]{BibTex-Key}` bzw. `\cite[S. 15-21]{BibTex-Key}` 

# Compilieren
Für das Paket _latexmk_ und die Erzeugung eines Glossars muss ein Perl-Interpreter installiert sein. Linux- und Mac-User haben normalerweise diesen schon im System installiert. Windows-Nutzern ist ActivePerl zu empfehlen (http://www.activestate.com/activeperl/downloads). Die Vorlage nutzt außerdem _biblatex_ mit dem Backend _biber_ für die Bibliographie.

## Über latexmk:
* Bauen: `latexmk`
* Aufräumen: `latexmk -c`

Oder über das makefile:
* Bauen: `make` oder `make all`
* Aufräumen:
  * `make clean` (entfernt output/, dokumentation.pdf und dokumentation.synctex.gz)
  * `make cleanup` (entfernt nur temporäre Build-Dateien)

## Ohne latexmk
Wenn kein latexmk installiert werden kann oder soll, stellt das makefile auch die entsprechenden Befehle ohne latexmk bereit: 
* `make all-legacy`
* `make clean-legacy`
* `make cleanup-legacy`

# Nur Deckblatt verwenden
```latex
% .....
\includepdf[pages=1]{../latexVorlage/dokumentation.pdf}
```

