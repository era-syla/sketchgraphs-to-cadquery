import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0311, 0.0535).lineTo(-0.0234, 0.0535).lineTo(-0.0234, 0.0605).lineTo(-0.0311, 0.0605).lineTo(-0.0311, 0.0535).close()
solid=wp_sketch0.add(loop0).extrude(-0.01223251154471163)
