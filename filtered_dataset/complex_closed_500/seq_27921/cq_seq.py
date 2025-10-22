import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00666, 0.09388).lineTo(0.01486, 0.09388).lineTo(0.01486, 0.08686).lineTo(0.00666, 0.08686).lineTo(0.00666, 0.09388).close()
solid=wp_sketch0.add(loop0).extrude(0.007236500712357446)
