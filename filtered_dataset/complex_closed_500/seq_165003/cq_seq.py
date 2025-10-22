import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.03953, 0.02453).lineTo(0.03716, 0.02154).lineTo(0.05684, 0.00793).lineTo(0.0784, 0.0).lineTo(0.08136, 0.00665).lineTo(0.04303, 0.02673).lineTo(0.03953, 0.02453).close()
solid=wp_sketch0.add(loop0).extrude(-0.0661993067099455)
