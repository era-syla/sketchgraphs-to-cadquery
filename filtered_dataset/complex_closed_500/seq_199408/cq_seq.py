import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.01, 0.0).lineTo(-0.01, 0.15).lineTo(0.09, 0.15).lineTo(0.09, 0.144).lineTo(0.087, 0.144).lineTo(0.087, 0.147).lineTo(-0.007, 0.147).lineTo(-0.007, 0.003).lineTo(0.0, 0.003).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.025787223526947223)
