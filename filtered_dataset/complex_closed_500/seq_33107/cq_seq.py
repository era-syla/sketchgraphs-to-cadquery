import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00058, -0.039).threePointArc((0.039, -0.0), (0.00058, 0.039)).lineTo(0.00058, -0.039).close()
solid=wp_sketch0.add(loop0).extrude(-0.08593680067694073)
