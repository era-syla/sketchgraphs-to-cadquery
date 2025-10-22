import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.375, 0.46).lineTo(0.375, 0.46).lineTo(0.375, -0.46).lineTo(-0.375, -0.46).lineTo(-0.375, 0.46).close()
solid=wp_sketch0.add(loop0).extrude(-1.2358377653070804)
