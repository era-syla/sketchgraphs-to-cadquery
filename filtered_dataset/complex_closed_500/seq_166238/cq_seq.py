import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.19064, -0.00894).lineTo(-0.19064, 0.04106).lineTo(-0.18564, 0.04106).lineTo(-0.18564, -0.00394).lineTo(-0.14064, -0.00394).lineTo(-0.14064, -0.00894).lineTo(-0.19064, -0.00894).close()
solid=wp_sketch0.add(loop0).extrude(-0.06455478272445282)
