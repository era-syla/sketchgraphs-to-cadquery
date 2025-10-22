import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01925, -0.017).lineTo(-0.02424, -0.013).lineTo(-0.02415, -0.016).lineTo(0.01935, -0.02).lineTo(0.01925, -0.017).close()
solid=wp_sketch0.add(loop0).extrude(0.046775069412160926)
