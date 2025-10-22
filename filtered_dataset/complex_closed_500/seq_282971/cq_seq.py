import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.12889, 0.0127).lineTo(-0.11111, 0.0127).lineTo(-0.11111, 0.00762).lineTo(-0.12889, 0.00762).lineTo(-0.12889, 0.0127).close()
solid=wp_sketch0.add(loop0).extrude(0.04519612520498619)
