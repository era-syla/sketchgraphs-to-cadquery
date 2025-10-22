import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0045, -0.001).lineTo(0.0045, -0.001).lineTo(0.0045, -0.007).lineTo(-0.0045, -0.007).lineTo(-0.0045, -0.001).close()
solid=wp_sketch0.add(loop0).extrude(0.010516192892695259)
