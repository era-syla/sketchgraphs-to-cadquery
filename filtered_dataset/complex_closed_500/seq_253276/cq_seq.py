import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05197, 0.05159).lineTo(0.04736, 0.05159).lineTo(0.04736, -0.05374).lineTo(-0.05197, -0.05374).lineTo(-0.05197, 0.05159).close()
solid=wp_sketch0.add(loop0).extrude(-0.18987483002263106)
