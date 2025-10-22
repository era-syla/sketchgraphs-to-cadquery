import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-1.2319, -0.35387).lineTo(-1.0414, -0.35387).lineTo(-1.0414, -0.69677).lineTo(-1.2319, -0.69677).lineTo(-1.2319, -0.35387).close()
solid=wp_sketch0.add(loop0).extrude(0.4120344152041243)
