import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0025, 0.00779).threePointArc((-0.016, 0.0), (-0.0025, -0.00779)).threePointArc((0.0, -0.00712), (0.0025, -0.00779)).threePointArc((0.016, 0.0), (0.0025, 0.00779)).threePointArc((0.0, 0.00712), (-0.0025, 0.00779)).close()
solid=wp_sketch0.add(loop0).extrude(0.010922276289462034)
