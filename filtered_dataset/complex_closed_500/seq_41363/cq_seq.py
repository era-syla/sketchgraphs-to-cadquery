import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05165, 0.01257).lineTo(-0.05165, -0.01257).threePointArc((-0.04961, -0.0181), (-0.04446, -0.02097)).threePointArc((0.0, -0.02442), (0.04446, -0.02097)).threePointArc((0.04961, -0.0181), (0.05165, -0.01257)).lineTo(0.05165, 0.01257).threePointArc((0.04961, 0.0181), (0.04446, 0.02097)).threePointArc((-0.0, 0.02442), (-0.04446, 0.02097)).threePointArc((-0.04961, 0.0181), (-0.05165, 0.01257)).close()
solid=wp_sketch0.add(loop0).extrude(-0.2734610986593129)
