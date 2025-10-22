import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0193, 0.0105).lineTo(0.0177, 0.0105).lineTo(0.0177, -0.0105).lineTo(0.0193, -0.0105).lineTo(0.0193, 0.0105).close()
solid=wp_sketch0.add(loop0).extrude(0.028641403220939724)
