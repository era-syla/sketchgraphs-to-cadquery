import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.54218, 0.0365).lineTo(-0.51818, 0.0365).lineTo(-0.51818, -0.2335).lineTo(-0.54218, -0.2335).lineTo(-0.54218, 0.0365).close()
solid=wp_sketch0.add(loop0).extrude(0.10761428873521331)
