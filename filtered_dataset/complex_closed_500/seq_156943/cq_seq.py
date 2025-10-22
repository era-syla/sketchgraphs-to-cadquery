import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0275, 0.0).lineTo(0.0275, 0.0).lineTo(0.0275, 0.007).threePointArc((0.0, 0.01073), (-0.0275, 0.007)).lineTo(-0.0275, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.13820799625532423)
