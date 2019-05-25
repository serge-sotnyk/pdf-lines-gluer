# PDF cleaner
This project aimed to preprocess PDF-extracted or other texts with paragraph termination
symbols, used as line endings and hard-hyphenations.

## How to use
Simple get https://github.com/serge-sotnyk/pdf-lines-gluer/blob/master/pdf_preprocessor.py 
and copy it to your project. After this, you can use functionality calling function
preprocess_pdf():

```python
from pdf_preprocessor import preprocess_pdf

text = """The rapid expansion of wireless services such as cellular voice, PCS
(Personal Communications Services), mobile data and wireless LANs
in recent years is an indication that signicant value is placed on accessibility
and portability as key features of telecommunication (Salkintzis and Mathiopoulos (Guest Ed.), 2000).
devices have maximum utility when they can be used any-
where at anytime". One of the greatest limitations to that goal, how-
ever, is nite power supplies. Since batteries provide limited power, a
general constraint of wireless communication is the short continuous
operation time of mobile terminals. Therefore, power management is
y Corresponding Author: Dr. Krishna Sivalingam. Part of the research was
supported by Air Force Oce of Scientic Research grants F-49620-97-1-
0471 and F-49620-99-1-0125; by Telcordia Technologies and by Intel. Part of
the work was done while the rst author was at Washington State Univer-
sity. The authors' can be reached at cej@bbn.com, krishna@eecs.wsu.edu,
pagrawal@research.telcordia.com, jcchen@research.telcordia.com
c
2001 Kluwer Academic Publishers. Printed in the Netherlands.
Jones, Sivalingam, Agrawal and Chen
one of the most challenging problems in wireless communication, and
recent research has addressed this topic (Bambos, 1998). Examples include
a collection of papers available in (Zorzi (Guest Ed.), 1998) and
a recent conference tutorial (Srivastava, 2000), both devoted to energy
ecient design of wireless networks.
Studies show that the signicant consumers of power in a typical
laptop are the microprocessor (CPU), liquid crystal display (LCD),
hard disk, system memory (DRAM), keyboard/mouse, CDROM drive,
oppy drive, I/O subsystem, and the wireless network interface card
(Udani and Smith, 1996, Stemm and Katz, 1997). A typical example
from a Toshiba 410 CDT mobile computer demonstrates that nearly
36% of power consumed is by the display, 21% by the CPU/memory,
18% by the wireless interface, and 18% by the hard drive. Consequently,
energy conservation has been largely considered in the hardware design
of the mobile terminal (Chandrakasan and Brodersen, 1995) and in
components such as CPU, disks, displays, etc. Signicant additional
power savings may result by incorporating low-power strategies into
the design of network protocols used for data communication. This
paper addresses the incorporation of energy conservation at all layers
of the protocol stack for wireless networks.
The remainder of this paper is organized as follows. Section 2 introduces
the network architectures and wireless protocol stack considered
in this paper. Low-power design within the physical layer is brie
y
discussed in Section 2.3. Sources of power consumption within mobile
terminals and general guidelines for reducing the power consumed are
presented in Section 3. Section 4 describes work dealing with energy
ecient protocols within the MAC layer of wireless networks, and
power conserving protocols within the LLC layer are addressed in Section
5. Section 6 discusses power aware protocols within the network
layer. Opportunities for saving battery power within the transport
layer are discussed in Section 7. Section 8 presents techniques at the
OS/middleware and application layers for energy ecient operation.
Finally, Section 9 summarizes and concludes the paper.
2. Background
This section describes the wireless network architectures considered in
this paper. Also, a discussion of the wireless protocol stack is included
along with a brief description of each individual protocol layer. The
physical layer is further discussed. """

print(preprocess_pdf(text))
```

Output:
```
The rapid expansion of wireless services such as cellular voice, PCS (Personal Communications Services), mobile data and wireless LANs in recent years is an indication that signicant value is placed on accessibility and portability as key features of telecommunication (Salkintzis and Mathiopoulos (Guest Ed.), 2000). devices have maximum utility when they can be used anywhere at anytime". One of the greatest limitations to that goal, however, is nite power supplies. Since batteries provide limited power, a general constraint of wireless communication is the short continuous operation time of mobile terminals. Therefore, power management is y Corresponding Author: Dr. Krishna Sivalingam. Part of the research was supported by Air Force Oce of Scientic Research grants F-49620-97-10471 and F-49620-99-1-0125; by Telcordia Technologies and by Intel. Part of the work was done while the rst author was at Washington State University. The authors' can be reached at cej@bbn.com, krishna@eecs.wsu.edu, pagrawal@research.telcordia.com, jcchen@research.telcordia.com
c 2001 Kluwer Academic Publishers. Printed in the Netherlands.
Jones, Sivalingam, Agrawal and Chen one of the most challenging problems in wireless communication, and recent research has addressed this topic (Bambos, 1998). Examples include a collection of papers available in (Zorzi (Guest Ed.), 1998) and a recent conference tutorial (Srivastava, 2000), both devoted to energy ecient design of wireless networks.
Studies show that the signicant consumers of power in a typical laptop are the microprocessor (CPU), liquid crystal display (LCD), hard disk, system memory (DRAM), keyboard/mouse, CDROM drive, oppy drive, I/O subsystem, and the wireless network interface card (Udani and Smith, 1996, Stemm and Katz, 1997). A typical example from a Toshiba 410 CDT mobile computer demonstrates that nearly 36% of power consumed is by the display, 21% by the CPU/memory, 18% by the wireless interface, and 18% by the hard drive. Consequently, energy conservation has been largely considered in the hardware design of the mobile terminal (Chandrakasan and Brodersen, 1995) and in components such as CPU, disks, displays, etc. Signicant additional power savings may result by incorporating low-power strategies into the design of network protocols used for data communication. This paper addresses the incorporation of energy conservation at all layers of the protocol stack for wireless networks.
The remainder of this paper is organized as follows. Section 2 introduces the network architectures and wireless protocol stack considered in this paper. Low-power design within the physical layer is brie
y discussed in Section 2.3. Sources of power consumption within mobile terminals and general guidelines for reducing the power consumed are presented in Section 3. Section 4 describes work dealing with energy ecient protocols within the MAC layer of wireless networks, and power conserving protocols within the LLC layer are addressed in Section
5. Section 6 discusses power aware protocols within the network layer. Opportunities for saving battery power within the transport layer are discussed in Section 7. Section 8 presents techniques at the OS/middleware and application layers for energy ecient operation.
Finally, Section 9 summarizes and concludes the paper.
2. Background
This section describes the wireless network architectures considered in this paper. Also, a discussion of the wireless protocol stack is included along with a brief description of each individual protocol layer. The physical layer is further discussed.
```

## How to train a classifier on your data

I don't use language dependent features so that you can try this classifier on any 
text written on Indo-European languages. Nevertheless, you can face troubles for 
your texts. If it occurs, you can train your new own classifier.

### Add more data

1. Add mode train data. Add text with mistakes into folder corpus and annotate it 
like file [corpus/1005058.txt](corpus/1005058.txt). Every file should contain the 
first symbol with mark, should we glue current line with the previous one or not 
('*' - leave as is, '+' - should be glued). Hyphenation processing is simple and 
hardcoded, so we don't need individual marks for it.
2. Run [pdf_gluer.ipynb](pdf_gluer.ipynb).
3. Get new [pdf_preprocessor.py](pdf_preprocessor.py) and check its quality for your 
task.

### Add new features

If new data doesn't help to reach enough quality, you can try to add new features. 
Please, look on [pdf_lines_gluer.py](pdf_lines_gluer.py). Here you can add code for
generating new features. Feel free to perform experiments! However, don't 
delete the following line:

```python
# inject code here #
```

It is important, because this file is also the template for autogenerated 
[pdf_preprocessor.py](pdf_preprocessor.py), and the mark is used as a mark to add 
autogenerated code.

