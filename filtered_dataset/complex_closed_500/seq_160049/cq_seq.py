import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02, 0.02).lineTo(0.0, 0.02).lineTo(-0.0, 0.0125).lineTo(-0.0025, 0.0125).threePointArc((-0.005, 0.01), (-0.0025, 0.0075)).lineTo(0.0, 0.0075).lineTo(0.0, -0.0).lineTo(0.02, 0.0).lineTo(0.02, 0.02).close()
solid=wp_sketch0.add(loop0).extrude(0.021866756767623355)
