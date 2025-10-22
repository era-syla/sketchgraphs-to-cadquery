import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04704, 0.02553).lineTo(-0.04704, 0.02553).lineTo(-0.04704, -0.02553).lineTo(0.04704, -0.02553).lineTo(0.04704, 0.02553).close()
solid=wp_sketch0.add(loop0).extrude(-0.11684575284260602)
