import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.18131, 0.04818).lineTo(0.17831, 0.04818).lineTo(0.17831, 0.04493).lineTo(0.18131, 0.04493).lineTo(0.18131, 0.04818).close()
solid=wp_sketch0.add(loop0).extrude(0.00872661066934435)
