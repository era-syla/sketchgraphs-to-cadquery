import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(11.684, 3.0734).lineTo(11.684, 3.8354).lineTo(12.446, 3.19601).lineTo(12.446, 3.0734).lineTo(11.684, 3.0734).close()
solid=wp_sketch0.add(loop0).extrude(-0.8932679390027402)
