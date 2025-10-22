import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.285, 0.29).threePointArc((-0.22727, 0.10535), (-0.065, 0.0)).lineTo(-0.055, 0.03).lineTo(0.0, 0.03).lineTo(0.0, 0.24).lineTo(-0.2216, 0.24).lineTo(-0.235, 0.29).lineTo(-0.285, 0.29).close()
solid=wp_sketch0.add(loop0).extrude(0.4667621044586129)
