import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.016, 0.09169).lineTo(-0.896, 0.09169).lineTo(-0.896, -0.11631).lineTo(-0.016, -0.11631).lineTo(-0.016, 0.09169).close()
solid=wp_sketch0.add(loop0).extrude(-1.0544513854369053)
