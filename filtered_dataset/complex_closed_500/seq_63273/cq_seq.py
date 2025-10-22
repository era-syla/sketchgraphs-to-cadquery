import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.07642, -0.12576).lineTo(0.08576, 0.1077).threePointArc((0.07479, 0.13211), (0.0487, 0.13805)).threePointArc((-0.0, 0.13221), (-0.0487, 0.13805)).threePointArc((-0.07479, 0.13211), (-0.08576, 0.1077)).lineTo(-0.07642, -0.12576).threePointArc((-0.07291, -0.13482), (-0.06458, -0.13983)).threePointArc((0.0, -0.14667), (0.06458, -0.13983)).threePointArc((0.07291, -0.13482), (0.07642, -0.12576)).close()
solid=wp_sketch0.add(loop0).extrude(-0.7375096711432317)
