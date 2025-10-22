import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.3174, 0.21449).lineTo(0.2922, 0.21449).lineTo(0.2922, -0.24271).lineTo(-0.3174, -0.24271).lineTo(-0.3174, 0.21449).close()
solid=wp_sketch0.add(loop0).extrude(0.8359150389195472)
