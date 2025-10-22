import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.05849, 0.02931).lineTo(0.02529, 0.02931).lineTo(0.02529, 0.00931).lineTo(0.05849, 0.00931).lineTo(0.05849, 0.02931).close()
solid=wp_sketch0.add(loop0).extrude(-0.05336795018123272)
