import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0331, 0.0127).lineTo(0.0331, 0.0127).threePointArc((0.03664, 0.01124), (0.0381, 0.0077)).lineTo(0.0381, -0.0077).threePointArc((0.03664, -0.01124), (0.0331, -0.0127)).lineTo(-0.0331, -0.0127).threePointArc((-0.03664, -0.01124), (-0.0381, -0.0077)).lineTo(-0.0381, 0.0077).threePointArc((-0.03664, 0.01124), (-0.0331, 0.0127)).close()
solid=wp_sketch0.add(loop0).extrude(-0.10265417514573144)
