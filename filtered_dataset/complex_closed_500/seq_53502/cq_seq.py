import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0508, -0.1524).lineTo(0.0508, -0.1524).threePointArc((0.10468, -0.13008), (0.127, -0.0762)).lineTo(0.127, 0.0762).threePointArc((0.10468, 0.13008), (0.0508, 0.1524)).lineTo(-0.0508, 0.1524).threePointArc((-0.10468, 0.13008), (-0.127, 0.0762)).lineTo(-0.127, -0.0762).threePointArc((-0.10468, -0.13008), (-0.0508, -0.1524)).close()
solid=wp_sketch0.add(loop0).extrude(0.7024040624740232)
