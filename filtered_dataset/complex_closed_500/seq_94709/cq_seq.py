import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01455, 0.005).lineTo(0.0147, 0.005).lineTo(0.0147, -0.005).lineTo(-0.01455, -0.005).lineTo(-0.01455, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(0.031792670564694044)
