import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-1.51892, 0.0).lineTo(-1.37434, 0.04819).lineTo(-1.3884, 0.09036).lineTo(-1.53298, 0.04217).lineTo(-1.51892, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.0710535509570762)
