import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02, -0.008).lineTo(-0.02, -0.008).lineTo(-0.02, 0.008).lineTo(0.02, 0.008).lineTo(0.02, -0.008).close()
solid=wp_sketch0.add(loop0).extrude(0.0008742711466649311)
