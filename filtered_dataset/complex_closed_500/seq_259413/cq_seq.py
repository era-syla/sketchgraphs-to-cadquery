import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02801, 0.00998).lineTo(-0.0441, 0.00998).lineTo(-0.0441, 0.00641).lineTo(-0.02801, 0.00641).lineTo(-0.02801, 0.00998).close()
solid=wp_sketch0.add(loop0).extrude(0.0038353097830205515)
