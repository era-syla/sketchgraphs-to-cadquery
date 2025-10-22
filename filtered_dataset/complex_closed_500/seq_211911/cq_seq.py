import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.605, 0.0).lineTo(0.59, 0.0).lineTo(0.59, 0.5).lineTo(0.605, 0.5).lineTo(0.605, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.968564126075897)
