import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-4.0, 0.5).lineTo(-3.9, 0.5).lineTo(-3.9, 0.4).lineTo(-4.0, 0.4).lineTo(-4.0, 0.5).close()
solid=wp_sketch0.add(loop0).extrude(0.03624601596593869)
