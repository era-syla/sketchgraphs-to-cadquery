import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0125, 0.0).threePointArc((0.0, 0.0125), (-0.0125, 0.0)).lineTo(-0.0025, 0.0).threePointArc((0.0, 0.0025), (0.0025, 0.0)).lineTo(0.0125, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.0035282911193535776)
