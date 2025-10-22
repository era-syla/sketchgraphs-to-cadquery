import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03059, 0.06749).lineTo(-0.01159, 0.06749).lineTo(-0.01159, 0.04849).lineTo(-0.03059, 0.04849).lineTo(-0.03059, 0.06749).close()
solid=wp_sketch0.add(loop0).extrude(-0.038168416992208826)
