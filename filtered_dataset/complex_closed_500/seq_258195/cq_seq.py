import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01264, -0.02162).lineTo(0.01264, -0.0217).lineTo(0.01259, -0.02167).lineTo(0.01264, -0.02162).close()
solid=wp_sketch0.add(loop0).extrude(-0.00012357838465734783)
