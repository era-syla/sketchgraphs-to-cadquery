import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(11.66007, 0.0).lineTo(12.46007, 0.0).lineTo(12.46007, 2.13).lineTo(11.66007, 2.13).lineTo(11.66007, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-4.8865614733324865)
