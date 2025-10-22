import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.12147, 0.01905).lineTo(-0.14687, 0.01905).threePointArc((-0.15136, 0.01719), (-0.15322, 0.0127)).lineTo(-0.15322, -0.0127).threePointArc((-0.15136, -0.01719), (-0.14687, -0.01905)).lineTo(-0.12147, -0.01905).threePointArc((-0.11698, -0.01719), (-0.11512, -0.0127)).lineTo(-0.11512, 0.0127).threePointArc((-0.11698, 0.01719), (-0.12147, 0.01905)).close()
solid=wp_sketch0.add(loop0).extrude(-0.08076025771100738)
