import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05054, 0.005).lineTo(-0.04934, 0.005).lineTo(-0.04979, 0.00455).lineTo(-0.05009, 0.00455).lineTo(-0.05054, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(0.0012352821898721988)
