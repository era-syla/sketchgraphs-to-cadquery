import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.10794, 0.0).lineTo(0.09524, 0.0).lineTo(0.09524, 0.0127).lineTo(0.10794, 0.0127).lineTo(0.10794, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.025074619142242224)
