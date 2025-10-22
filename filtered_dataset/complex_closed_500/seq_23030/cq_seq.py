import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(3.475, 0.0).lineTo(4.185, 0.0).lineTo(4.185, 0.2).lineTo(3.475, 0.2).lineTo(3.475, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(1.1547267499220184)
