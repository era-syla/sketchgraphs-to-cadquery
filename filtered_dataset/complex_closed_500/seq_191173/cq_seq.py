import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 1.77386).lineTo(1.0, 1.77386).lineTo(1.0, 2.04386).lineTo(-0.0, 2.04386).lineTo(0.0, 1.77386).close()
solid=wp_sketch0.add(loop0).extrude(-0.03799497845230082)
