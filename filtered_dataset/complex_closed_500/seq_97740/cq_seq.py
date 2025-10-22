import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0035, 0.003).lineTo(-0.0035, 0.0).lineTo(0.0035, 0.0).lineTo(0.0035, 0.003).threePointArc((-0.0, 0.005), (-0.0035, 0.003)).close()
solid=wp_sketch0.add(loop0).extrude(0.015464744607892567)
