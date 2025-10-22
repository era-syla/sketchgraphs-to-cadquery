import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00454, 0.00231).threePointArc((-0.00336, -0.00052), (-0.00054, -0.00169)).lineTo(0.00054, -0.00169).threePointArc((0.00337, -0.00052), (0.00454, 0.00231)).lineTo(-0.00454, 0.00231).close()
solid=wp_sketch0.add(loop0).extrude(-0.013116264094425225)
