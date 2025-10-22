import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05863, -0.10154).lineTo(-0.05403, -0.10614).lineTo(-0.05545, -0.10755).lineTo(-0.06004, -0.10295).lineTo(-0.05863, -0.10154).close()
solid=wp_sketch0.add(loop0).extrude(0.013191123193878882)
