import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.4572, 0.4572).lineTo(0.4572, 0.4572).threePointArc((-0.0, 0.9144), (-0.4572, 0.4572)).close()
solid=wp_sketch0.add(loop0).extrude(-1.279218412286764)
